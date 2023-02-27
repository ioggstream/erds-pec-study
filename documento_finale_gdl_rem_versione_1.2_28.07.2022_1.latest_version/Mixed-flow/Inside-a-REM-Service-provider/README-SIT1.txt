Scenario with the following properties:
 * Four recipients: recipientA, recipientB, recipientC, recipientD
 * Two of these recipents, (recipientA & recipientB) are subscribed to S1-REMS (the sender's REMS)
 * The other two (recipientC & recipientD) are subscribed to R2-REMS.
 * The recipients (recipientC & recipientD) are in Cc: to the original message submitted by the sender.
 * The transaction inside the same REMS (S1-REMS) doesn't issue/send any Relay recept but only ContentConsignment receipts.
 * Any recipient has own <tns:Identity> element actually present only when, for that event, such information is available. Empty in the other cases.
 * The numbers on each folder give some idea on the time sequence any event can occour.
 * The name of each folder and/or each file is self explanatory.
 * Each folder contains the REM messages involved in some particular event and a readme with a short summary.
