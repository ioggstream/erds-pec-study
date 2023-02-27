# Flussi

I diagrammi
TUC2/EME1, TUC2/EME2, TUC3/EME3
descrivono la parte più
generale dei flussi, mentre le particolarità (es.
i sotto flussi opzionali e/o gli errori gestiti)
sono riportati in Figure 9, Figure 10, Figure
11, Figure 12, Figure 13 e Figure 14.


## Registered to unregisterd users

```mermaid
---
title: Outflow from registered to unregistered users TUC2/EME1
---
sequenceDiagram
    %% Actors
    actor A as Registered Sender
    participant S as S-REMS
    participant E as non-ERDS
    actor B as Unregistered Recipient

    %% Sender to S-REMS
    activate A
    A->>A: Compose the <br> original message
    activate A
    A->>S: Submit the <br> original message
    deactivate A
    activate S
    S->>S: Compose the<br>SubmissionAcceptance<br>REM receipt
    activate S
    S-->>S: Make it available to the senders's mailbox
    deactivate S
    activate A
    A->>S: Retrieve the SubmissionAcceptance REM receipt
    activate S
    S-->>A: ""
    deactivate S
    deactivate A
    deactivate A

    %% S-REMS to non-ERDS
    S->>S: Compose the <br> REM dispatch
    activate S
    S->>E: Relay the <br> REM dispatch
    deactivate S
    deactivate S
    activate E
    E->>E: Accept REM dispatch
    activate E
    E->>E: Consign the <br> REM dispatch to UR-mailbox
    deactivate E
    activate B
    B->>E: Retrieve the REM dispatch
    E-->>B: ""
    deactivate B
    deactivate E

```

## Outflow from registered to unregistered users failure TUC2/EME2

```mermaid
---
title: Outflow from registered to unregistered users failure TUC2/EME2
---
sequenceDiagram
    %% Actors
    actor A as Registered Sender
    participant S as S-REMS
    participant E as non-ERDS
    actor B as Unregistered Recipient

    %% Sender to S-REMS
    activate A
    A->>A: Compose the <br> original message
        activate A
        A->>S: Submit the <br> original message
        deactivate A

    activate S
    S->>S: Compose the<br>SubmissionAcceptance<br>REM receipt
        activate S
        S-->>S: Make it available to the senders's mailbox
        deactivate S

        activate A
        A->>S: Retrieve the SubmissionAcceptance REM receipt
            activate S
            S-->>A: ""
            deactivate S
        deactivate A

    %% S-REMS to non-ERDS
    S->>S: Compose the <br> REM dispatch
        activate S
        S-->>E: Relay the <br> REM dispatch
        S->>S: & Compose the <br> RelayToNonERDSFailure <br> REM receipt
        S-->>S: & Make it available to the senders's mailbox
        deactivate S

        activate A
        A ->>A: Retrieve the <br> RelayToNonERDSFailure <br> REM receipt
            activate S
            A-->>A: ""
            deactivate S
        deactivate A

    deactivate S
    deactivate A
```
## : Inflow from unregistered to registered users (TUC3/EME3)

```mermaid
---
title: Inflow from unregistered to registered users (TUC3/EME3)
---
sequenceDiagram
    %% Actors
    actor A as Unregistered Sender
    participant E as non-ERDS
    participant R as R-REMS
    actor B as Registered Recipient

    %% Sender to non-ERDS
    activate A
    A->>A: Compose the <br> original message
    activate A
    A->>E: Submit the <br> original message
    deactivate A
    deactivate A

    activate E
    E->>R: Relay the <br> original message
    deactivate E

    activate R
    R->>R: Accept the <br> original message
    activate R
    R->>R: Compose the <br> ReceivedFromNonERDS <br> REM dispatch
    deactivate R

    R->>R: Consign the <br> ReceivedFromNonERDS <br> to Registered-Recipient mailbox
    activate R
    deactivate R
    deactivate R

    activate B
    B->>R: Retrieve the <br> ReceivedFromNonERDS <br> REM dispatch
    activate R
    R-->>B: ""
    deactivate R
    deactivate B

```
