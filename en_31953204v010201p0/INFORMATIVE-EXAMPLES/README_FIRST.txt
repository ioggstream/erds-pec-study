********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* *********
                                               R E A D M E     F I R S T
********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* *********

As per EN 319 532-4, clause D.4.5 the present kit represents a complete set of working examples miming significant scenarios of
REM baseline.

The set of examples are contained in the ZIP attachment accompanying the EN 319 532-4 document.

These examples are organazed as follows:
<FILE>         README_FIRST.txt
<DIR>          SCENARIOS
<DIR>          CERTIFICATES
<DIR>          COMMON_SERVICE_INTERFACE
<DIR>          POINTS_OF_ATTENTION

Note 1: Any of the files present in the SCENARIOS subfolders are in EML text format. 
        So, other than they can be opened with a usual email client, they are
        also editable by a normal text editor. This property is true also for all
        the digital certificate files.
Note 2: The EML files are signed according to CAdES-B format on the S/MIME pkcs#7 
        digital signature.
Note 3: Any ERDS evidence attached as MIME body part in such EML is digital signed
        according to XAdES-B-T format (that is including a standard timestamp).

********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* *********

README_FIRST.txt: the present file

********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* *********

SCENARIOS: folder containing a number of scenarios S1..S7 organized in relevant subfolders.

 Any of these has:

  1. a well defined diagram named as <scenario name>.png
  2. a folder/subfolder structure containing all the REM messages exemplifying the relevant steps of the scenario

  There is a full correspondence between the diagram and the steps:
    - a Tag like (1a), (2a), (3b) etc. identifies any step.
    - it is formed by a number. Steps under equal numbers represent all the operations that can be performed, 
      in parallel, even at the same time regardless a predefined order: e.g. steps (7a), (7b), (7c) can be 
      executed in parallel and without any regard to the order.
      The subfix a,b, etc. sometimes represents a correlated path. For example 1a, 2a, 3a, are sequential steps
      of a direction of the information. If "Ante" subfix is used, this means that such step is just before the
      subsequent step: e.g. (3aAnte), is just before step (3a) 
    - These tags represents a biunivocal reference between the steps on the diagram and the relevant step on
      the scenario containing the REM messages examples. 
      E.g. the folder: 
         "S5/5b+5c.Returned_by_R-REMS-B_to_S-REMS-A" refers to the scenario S5 and contains the two REM receipts RB01 and RB21:
            (5b) Return RelayAcceptance RB01 REM receipt (rcp1@rb-rems.rem) and 
            (5c) Return RelayRejection  RB21 REM receipt (rcp2@rcp2domain.rem)
         Furthermore, the there is a full correspondence with the steps (5b) and (5c) of the diagram S5.png that
         gives a global view of the entire scenario S5 and so, in particular, also of such steps.

      It is suggested to follow any subfolder scenario, step by step, in parallel with the relevant figure.

Note 4: The same EML filename in two subfolders of the same scenario means that the content is the same.
        E.g. the file "REM_Dispatch.RA01.eml" under any subfolder of the scenario S1 is always the same
        object. It has been copied in the subfolders to mimic something like a "step-by-step" sequence of
        events (taking, ideally, a photo of each significant step).
        While, a suffix after a event name in each filename means that such REM receipt refers to the 
        recipient identified by such suffix.
        E.g. REM_RelayAcceptance3.RB01 means that it refers to the recipient nr. 3, and
             REM_RelayFailure1,2.RB02 means that it refers to the recipients nr. 1 and 2.
 
Note 5: In both scenario figures and folder/structure messages etc. the terms "ERD/ERDS" and "REM/REMS" are used
        in an equivalent way. Often the terms REM/REMS are used instad of "ERD/ERDS" because seem more pertinent
        being these examples in the context of REM baseline.

********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* *********
CERTIFICATES:

This folder contains the *TEST* certificates used to sign the all the REM messages present in any scenario.
These are represented in two formats:
  * Syntetical view, in pretty text format, with the main properties of any certificate.
  * classical base64 full certificate format


The "GlobalERDS Root CA" self-signed ROOT certificate (file REM-ROOT-CA.crt) has been used to sign the intermediate 
digital certificate.
 
The "GlobalERDS Intermediate CA" digital certificate (file REM-INTERMEDIATE-CA.crt) has been used to sign all
the signing "leaf" digital certificates (one for each test REMSP): 
  S-REMS-A-CERTIFICATE (sender REMS A)
  R-REMS-B-CERTIFICATE (recipient REMS B)
  R-REMS-C-CERTIFICATE (recipient REMS C)

The TSA.NOWNTSTS202004.pem represents the public part of the certificates chain used in the timestamp application, according
to XAdES-B-T, to any ERDS evidence.

Note: importing the "GlobalERDS Root CA" certificate in own computer, all the digital signatures of the REM messages present 
in  SCENARIOS/sub-folders will be verified, avoid any warning, by own email client.

********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* *********
COMMON_SERVICE_INTERFACE

This folder contains three triples, TL & CSI & DNS, of examples composing the Trusted List, the Common Service Interface XML data structures and the DNS configuration, each for any REMSP:
 
  TL_CCA & CSI_CCA (sender REMS A)
  TL_CCB & CSI_CCB (recipient REMS B)
  TL_CCC & CSI_CCC (recipient REMS C)

********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* *********
POINTS_OF_ATTENTION
This folder contains some additional info that needs to be taken in consideration during the check phases.
 
********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* ********* *********
