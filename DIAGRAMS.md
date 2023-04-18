# REM

**NON UFFICIALE**

Diagrammi di esempio delle relazioni tra le entità definite nel glossario REM.

## Glossario


```mermaid
graph LR

subgraph UserInteraction
sender[fa:fa-user sender]
recipient[fa:fa-user recipient]
end

subgraph REM_Service
REM:S-REM
REM:R-REM
REM:S
end

subgraph Organizzazione
REM:ID
REM:ID_Authority[Authority fa:fa-building] -->|governs| REM:ID
REM:Policy_IT[REM-Policy-IT\nRegole tecniche fa:fa-scroll] -.->|a| REM:ID_Policy
ERDS[Electronic Registered\nDelivery Service]
REM:S[REMS - Service]
REM:SP[Service Provider fa:fa-building]
REM:S-REMS[REMS - Sender\nService]
REM:R-REMS[REMR - Recipient\nService]
REM:TL[Trusted List fa:fa-scroll]
REM:C[Certificate fa:fa-key]
TSP[TSP fa:fa-building]
LOTL[List of\n Trusted Lists fa:fa-scroll fa:fa-scroll]
UserInteraction
TSA[Time Stamp Authority fa:fa-clockfa:fa-building]
TSC[Time Stamp Certificate fa:fa-clock]

REM_Service
end

sender -->|uses| REM:S-REMS
recipient -->|uses| REM:R-REMS

sender -->|sends UserContent to| recipient

REM:S -.->|a| ERDS
REM:S -->|generates| ERDS:Evidence -->|signed by| REM:C
REM:SP -->|complies with| REM:ID_Policy

REM:S-REMS & REM:R-REMS -.-> |a| REM:S -->|managed by a| REM:SP

REM:S-REMS-->|sends fa:fa-envelope to| REM:R-REMS
REM:TL -->|managed by| REM:SP
REM:SP -.->|a| TSP
REM:SP --o|downloads| LOTL

REM:S --o|uses| TSC -->|managed by| TSA
REM:S -->|owns| REM:C -->|managed by| REM:SP


%% REM vs PEC
subgraph PEC
PEC:IGPEC[IGPEC Indice Gestori PEC fa:fa-scroll]
PEC:SP
PEC:S
PEC:domain
PEC:busta

subgraph messaggi
PEC:accettazione
PEC:consegna

subgraph errori
PEC:e-non-accettazione
PEC:e-mancata-consegna
PEC:e-peo
PEC:e-timeout
end
end

end

PEC:IGPEC--> REM:TL
PEC:SP   --> REM:SP

PEC:S -->|managed by| PEC:SP
PEC:S -->|manages 1..n| PEC:domain
PEC:domain -->|uses| DNS:MX
```

## Imbustamenti


Tabella 1 – Corrispondenza tra tipi messaggi PEC vs REM

|PEC|REM|
|---|---|
|Busta di Trasporto |REM dispatch
|Ricevuta di Accettazione |SubmissionAcceptance|
Ricevuta di Avvenuta Consegna| ContentConsignment|
|Avviso di non accettazione|SubmissionRejection|
|Avviso di mancata consegna (errore-consegna)|ContentConsignmentFailure / RelayFailure|
|Busta di anomalia (messaggio di posta ordinaria)|ReceivedFromNonERDS|
|Avviso mancata consegna (superamento tempi massimi previsti, 12h,24h)|ContentConsignmentFailure / RelayFailure(prevista solo per il tempolimite delle 24h)|

Q: Le REM:Receipt sono tutte e sole quelle associate alle ricevute?

```mermaid
graph LR

Dispatch & Receipt -.-> |a| REM:Envelope -->|contains| REM:Headers
%% https://www.etsi.org/deliver/etsi_en/319500_319599/31953204/01.01.07_20/en_31953204v010107a.pdf
RelayMetadata -.-> |a| REM:Headers
Dispatch -->|contains| REM:Headers & UserContent & RelayMetadata  & ERDS:Evidence
Receipt -->|contains| REM:Headers & RelayMetadata & ERDS:Evidence
ERDS:Evidence -.-o|"hash of (Dispatch)"| UserContent
ERDS:Evidence -->|contains| Timestamp
ERDS:Evidence -.-o|contains| REM:Headers

click RelayMetadata "https://www.etsi.org/deliver/etsi_en/319500_319599/31953204/01.01.07_20/en_31953204v010107a.pdf#p=14"

```


## Daticert vs ERDS Evidence

La struttura dei messaggi REM e PEC è simile:

1. il media type è `multipart/signed; protocol="application/pkcs7-signature"` che contiene:

    a. un `multipart/mixed`

    b. una pcks7-signature (smime.p7s)

2. il multipart/mixed 1.a. contiene:

    a. un preambolo (REM introduction / PEC introduction)

    b. un XML con dei dati certificati (daticert.xml o ERDS:Evidence)

```mermaid
graph

subgraph signed_message["multipart/signed;<br> prototocol=application/pkcs7-signature<br>name=smime.p7s"]
end

subgraph body["body multipart/mixed"]
preambolo[REM/PEC Introduction<br>multipart/alternative]
metadati["daticert.xml o ERDS:Evidence<br>application/xml"]
end

subgraph message["multipart/signed; prototocol=application/pkcs7-signature"]
mime_headers
body
original_message["Original message (dispatch)<br>message/rfc822; <br>name=postacert.eml / AttachedMimeMessage"]
signed_message
end
```

A differenza della PEC:

1. il daticert.xml non è firmato, ma si basa sulla firma del messaggio completo. Invece l'ERFS:Evidence è firmata.
2. la REM supporta una ulteriore sezione chiamata REM:Extension con media type `xml` o `octect-stream`. Questa sezione viene utilizzata dal profilo italiano `rem-policy-it` per inserire ulteriori informazioni non supportate dal profilo REM base.
