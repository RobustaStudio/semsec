const crypto = require('crypto');
const https = require('https');

// ruleid: robusta-js-crypto-createcipher
const c1 = crypto.createCipher('aes-256-cbc', key);
// ok: robusta-js-crypto-createcipher
const c2 = crypto.createCipheriv('aes-256-gcm', key, iv);

// ruleid: robusta-js-crypto-math-random-token
const resetToken = Math.random().toString(36).slice(2);
// ok: robusta-js-crypto-math-random-token
const sessionId = crypto.randomBytes(32).toString('hex');

// ruleid: robusta-js-tls-reject-unauthorized
process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";
// ruleid: robusta-js-tls-reject-unauthorized
const agent = new https.Agent({rejectUnauthorized: false});
