Scenario with the following properties:
 * Four recipients: recipientC, recipientD, recipientE, recipientF
 * Two of these recipents, (recipientC & recipientE) are correctly subscribed to R2-REMS
 * The other two (recipientD & recipientF) are not subscribed to R2-REMS, even if their email domain leads to R2-REMS.
 * For some reason the REM dispatch is split in two identical REM dispatches (split1 & split2) sent separately to R2-REMS
 * R2-REMS manages the received dispatches according to the forward & reverse path of the SMTP transaction:
    * recipientC & recipientD for the REM dispatch split1
    * recipientE & recipientF for the REM dispatch split2
 * Two different relay responses are sent for split1 (one is an acceptance and anoter one a rejection)
 * Two different relay responses are sent for split2 (one is an acceptance and anoter one a rejection)
 * Each of these RelayAcceptance / RelayRejection REM receipt is tailored for a particular recipient (i.e. it has the
    <ext:RelayEvidenceRefersTo> element set to the recipient whose the relay evidence refers to, according with its semantic).
    As another example, a case of 9 recipients, 3 REM-dispatches split (each with 3 recipients) can generate any combination answers like:
      - 3 REM RelayAcceptance, one for each split, (without RelayEvidenceRefersTo): this means that everything is accepted or
          or
      - 2 REM RelayAcceptance for split 1 & split 2 (without RelayEvidenceRefersTo): this means that everything is accepted for recipients of split 1 & 2 and
      - 1 REM RelayRejection for 2 recipients of split 3 (wiht two RelayEvidenceRefersTo each referencing one of the two failing recipients) and
      - 1 REM RelayAcceptance for 1 recipients of split 3 (wiht one RelayEvidenceRefersTo referencing the successfully accepted recipients)
          or
      - any other combination respecting the semantic of RelayEvidenceRefersTo and maintaining the logical consistency
 * Any recipient has own <tns:Identity> element actually present only when, for that event, such information is available. Empty in the other cases.
 * The numbers on each folder give some idea on the time sequence any event can occour.
 * The name of each folder and/or each file is self explanatory.
 * Each folder contains the REM messages involved in some particular event and a readme with a short summary.
