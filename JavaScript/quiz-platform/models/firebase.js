const firebase = require('firebase/app');
require('firebase/auth');
require('firebase/firestore');

require('dotenv').config()

const creds = {
    apiKey: process.env.API_KEY,
    authDomain: process.env.AUTH_DOMAIN,
    projectId: process.env.PROJECT_ID,
    storageBucket: process.env.STORAGE_BUCKET,
    messagingSenderId: process.env.MESSAGING_SENDER_ID,
    appId: process.env.APP_ID,
    measurementId: process.env.MEASUREMENT_ID
}

let fbApp = firebase.initializeApp(creds);
module.exports = fbApp;