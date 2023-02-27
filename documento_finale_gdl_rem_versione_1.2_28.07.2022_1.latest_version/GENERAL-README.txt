
See § 2.7 Esempi di formati REM | Examples of REM formats 
 of the document
      "REM SERVICES – ETSI standard adoption criteria – Policy-IT 1.2 [28 luglio 2022]" 
 for more details of these examples.

The name of each folder and/or each file is self explanatory and can contain some additional readme.

* certificates folder: 
   The  "REM-ROOT-CA.crt" is a self-signed ROOT certificate, used to sign the intermediate digital certificates.
   The "REM-POLICY-IT-INTERMEDIATE-CERTIFICATE.crt" intermediate certificate is used to sign the 
   S1-REM-POLICY-IT-CERTIFICATE (sender's REMS) and R2-REM-POLICY-IT-CERTIFICATE.crt (recipient's REMS). 
   These allow, if imported, to not have any warnings when opening the REM messages (Dispatch and or Receipts) with a normal email client. 

   They are only for tests purposes. After the test they can be uninstalled.

   The two following certificates (seen as chain Intermediate + Leaf) are used to sign the REM messages EMLs and the 
   ERDS evidence XMLs of the examples. 
     - S1-REM-POLICY-IT-CERTIFICATE
       --  REM-POLICY-IT-INTERMEDIATE-CERTIFICATE.crt

     - R2-REM-POLICY-IT-CERTIFICATE.crt
       -- REM-POLICY-IT-INTERMEDIATE-CERTIFICATE.crt

   Any of the above certificate is in PEM base64 format.

* scenarios, flows & REM message folders:

   The folders contain a set of REM message EMLs examples (REM Dispatch & REM Receipts). 
   These are signed according to CAdES-B and using the aforementioned certificates.

   Any of these files is in EML text format. So, other than they can be opened with 
   a usual email client, they are also editable by a normal text editor.

* standalone-evidence folder:

   Any REM message of the Intra-REM-flow or Inflow or Outflow folder has a corresponding 
   ERDS evidence as attachment that is exactly one of that listed in standalone-evidence folder.
   These are signed according to XAdES-B-T using the aforementioned certificates and a time-stamp test service.

*****************************************************************************************************************
CAUTION: All the material (examples, certificates, scenarios, etc.) of the present deliverable is provided for 
examples and study purposes only on how it's reasonable to implement particular cases of REM services, and it 
contains only informative elements.
*****************************************************************************************************************

