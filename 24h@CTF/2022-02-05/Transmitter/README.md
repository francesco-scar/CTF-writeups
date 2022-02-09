# 24h@CTF Transmitter Writeup

## Category

Blockchain

## Description

The challenge give the text:

`0x7BB2B3F29faC32dd86b2B760ca180462b2E08e6E@Ropsten`

The description gives some hints about some important messages mixed with junk messages, communication between sailors during an emergency and the needing to convert some hex to get the flag.

## Writeup

Searching the given text in a search engine we find out that it is the id of a Ropsten Ethereum (crypto-currency based on blockchain) contract, so the blocks are publicly accessible.

Using the website [ropsten.etherscan.io](https://ropsten.etherscan.io) and [searching](https://ropsten.etherscan.io/address/0x7bb2b3f29fac32dd86b2b760ca180462b2e08e6e) the given id, you can find the [first transaction](https://ropsten.etherscan.io/tx/0x4268e5c9b9c87f869753a0cb33078872a84f6860f7d8f2dbbbedf74f910b75fd) to the specified account.

Checking the Logs for each transaction you can find that sometimes the data sections contains a message with only dots and dashes.

![First morse transaction](Ropsten_Transaction_Etherscan.png?raw=true)

Passing through all the transactions and writing down only the payload with dots and dashes you will get the following morse message:

```
....- -.... ....- -.-. ....- .----
....- --... --... -... ..... --...
...-- ...-- ....- -.-. ....- ...--
...-- ----- ....- -.. ...-- ...--
..... ..-. ..... ....- ...-- -----
..... ..-. ....- ..... ...-- --...
....- ---.. ...-- ...-- ..... ..---
....- ..... ..... ..... ....- -..
..... ..-. ..... ---.. ..... ---..
...-- .---- ....- ...-- ..... --...
-.... ---.. -.... ----. ..... --...
...-- ----- -.... ....- ..... -....
-.... -.... --... -..
```

Which decoded into text gives:

`464C41477B57334C43304D335F54305F453748335245554D5F5858314357686957306456667D`

Which decoded from hex to ascii chars give the flag:

`FLAG{W3LC0M3_T0_E7H3REUM_XX1CWhiW0dVf}`

## Flag

`FLAG{W3LC0M3_T0_E7H3REUM_XX1CWhiW0dVf}`

<hr>

If you find errors or you want to contribute to this writeup go to the [GitHub repository](https://github.com/francesco-scar/CTF-writeups/tree/main/24h%40CTF/2022-02-05/Cassette_track_A) or contact me [opening an issue](https://github.com/francesco-scar/CTF-writeups/issues)
