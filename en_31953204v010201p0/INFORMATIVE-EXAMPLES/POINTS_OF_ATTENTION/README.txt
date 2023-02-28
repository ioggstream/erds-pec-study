
There are two attention points regarding the preparation of original message to attach to
the REM dispatch.

Other than the security checks on it before to instill it in the REM circuit, (e.g. detecting 
abuses by presence of phishing/viruses/malware etc. as per EN 319 532-4, clause D.4.3 ) it is 
important to be sure of the format (CRLF terminated lines) and so that it ends with the 
CRLF 0d0a sequence (see below the hexdump example of the terminal part of the original message):

00000220  0d 0a 20 20 20 45 54 53  49 20 45 4e 20 33 31 39  |..   ETSI EN 319|
00000230  20 35 33 32 2d 34 20 75  70 64 61 74 65 64 20 77  | 532-4 updated w|
00000240  69 74 68 20 74 68 65 20  52 45 4d 20 62 61 73 65  |ith the REM base|
00000250  6c 69 6e 65 2e 0d 0a   <--------                  |line...|
00000257

Often can happen that the digest check is computed without final CRLF and so it is apparently
different (See  EN 319 532-4, clause C.4.5.1, Table C.22 item c/V./ii.)

******* ******* ******* ******* ******* ******* ******* ******* ******* ******* ******* *******

Another attention point is when the original message is attached inside the REM dispatch as rfc822 message media type MIME part.
In fact two CRLFs/line breaks appear in the MIME stream at the end of such part: the first is composed by the 0x0D0A sequence 
(representing the end-of-file of the original message), and the second CRLF is due to the requirement prescribed in 
IETF RFC 2046 [i.14] clause 5.1.1: put any boundary (and so also the epilogue of the original message) at the beginning of the line.

The unambiguous individuation of the correct portion representing the original message (that clearly ends 
with the first CRLF) inside the REM dispatch is fundamental during the check phases of the "digest".

See below a portion of a REM dispatch:

------=_Part_26335064_5BC4B109E.1481841694172                          <----- Boundary of MIME part
Content-Type: message/rfc822; name=AttachedMimeMessage                 <----- REM dispacth MIME part header 
Content-Transfer-Encoding: binary                                      <----- REM dispacth MIME part header
Content-Disposition: attachment; filename=AttachedMimeMessage          <----- REM dispacth MIME part header
REM-Section-Type: rem_message/original                                 <----- REM dispacth MIME part header
                                                                       <----- CRLF separation 
From: "Sender name" <sender@senderdomain.rem>                          <----- START OF original message
To: <rcp1@rb-rems.rem>, <rcp2@rcp2domain.rem>, <rcp3@rc-rems.rem>, <rcp4@non-rem-domain.nrem>
Subject: Purchase order #1237
Date: Sat, 20 Nov 2021 19:10:16 +0100
Message-ID: <26A0CF65.00566CE0.7297C835.85251369.rem-service@sa-rems.rem>
REM-UAMessageIdentifier: <30be01d30072$7297c835$f9b72bf0$@de>
Content-Type: text/plain; charset=UTF-8

   This is the user's body of the original message built taking inspiration
   from the examples and figures present in ETSI EN 319 532-3 and in the
   ETSI EN 319 532-4 updated with the REM baseline.                    <----- FIRST CRLF(0d0a) at the end of the last original message's line
                                                                       <----- SECOND CRLF as per RFC 2046
------=_Part_26335064_5BC4B109E.1481841694172                          <----- Boundary of the next MIME part, etc.
Content-Type: application/xml; charset=UTF-8; name="SubmissionAcceptance.xml";

Note: the original message on which is computed the digest (and on which recalculate it, for a posteriori check) ends precisely with the first CRLF.
******* ******* ******* ******* ******* ******* ******* ******* ******* ******* ******* *******

XAdES-B-T digital signature of any ERDS evidence and CAdES-B digital signature (S/MIME pkcs7) of any REM message:

These digital signatures are made both using the same couple of digital certificates: 

 1. signing leaf certificate & 
 2. intermediate digital certificate. 

This facilitate one of the automatic validation phases: that of the REMS software and/or of the user's email client
starting from the signing leaf certificate, througn the intermediate (also incorporated in the signature) and ending
with the root-CA of the entire certification path (normally installed in any OS software).

Furthermore, any signing leaf certificates is contained in the TL at the following element of any REMSP:
        <TSPService>
          <ServiceInformation>
            <ServiceDigitalIdentity>
              <DigitalId>
                <X509Certificate> ... </X509Certificate>

This introduces a further security anchor representing a comprehensive cross certification system.

******* ******* ******* ******* ******* ******* ******* ******* ******* ******* ******* *******

In the ERDS evidence XMLs attached with the REM receipts of the various scenarios, often can happen that
the element:
      <tns:Identity>
                <saml:Attribute> ...
                </saml:Attribute>
      </tns:Identity>

relevant to the recipient(s) is present or absent.
There is a rational based on the certain aspects about why the example want to outline this condition:
In fact, the identity data of a user are typically known and managed by the REMSP where the user is registered.
In case of the recipient(s), such data can be authoritatively incorporated in the ERDS evidence issued by the
R-REMSP that is competent for any particular recipient. So, for example, S-REMS should not have authoritative
data of recipients issuing SubmissionAcceptance ERDS evidence. Whereas, a R-REMS can fill the Identity element
relevant to the recipient(s) for which it is competent during issuing some ERDS evidence. Thus, a RelayAcceptance
or a ContentConsignment ERDS evidence can have the presence of both Sender's and Recipient's Identity elements.

******* ******* ******* ******* ******* ******* ******* ******* ******* ******* ******* *******
