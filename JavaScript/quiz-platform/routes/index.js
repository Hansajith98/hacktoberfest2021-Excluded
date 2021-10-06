const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const localStorage = require('local-storage');
const fbApp = require('../models/firebase');

const router = express.Router();
const app = express();
router.use(bodyParser.urlencoded())
db = fbApp.firestore();

require('dotenv').config();

let msEndpoint = ''

router.get('/', (req, res) => {
	const scope =  process.env.SCOPES.replace(/\s/g, "%20");
	msEndpoint = `https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?client_id=${process.env.CLIENT_ID}&response_type=code&redirect_uri=${process.env.REDIRECT_URI}&response_mode=query&scope=${scope}&state=00042`
	return res.render('index', {data: {endPoint: msEndpoint, currentUser: false}})
})

router.get('/redirect', (req, res) => {
	const code = req.query.code
	const tokenEndpoint = "https://login.microsoftonline.com/organizations/oauth2/v2.0/token"
	const creds = {
		client_id: process.env.CLIENT_ID,
		client_secret: process.env.CLIENT_SECRET,
		redirect_uri: process.env.REDIRECT_URI,
		grant_type: 'authorization_code',
		scope: process.env.SCOPES,
		code: code
	}

	const params = new URLSearchParams();
	for (i in creds){
		params.append(`${i}`, `${creds[i]}`)
	}

	const config = {
		headers: {
		  'Content-Type': 'application/x-www-form-urlencoded'
		}
	  }

	axios.post(tokenEndpoint, params, config).then((response) => {
		const accessToken = response.data.access_token;
		const configr = {headers: {'Authorization': `Bearer ${accessToken}`}}
		axios.post('https://graph.microsoft.com/oidc/userinfo', {}, configr).then((resp) => {

			localStorage("userDetails", JSON.stringify(resp.data));
			
			db.collection('users').doc(resp.data.email).get()
			.then((doc) => {
				if (doc.exists){
					// module.exports = {
					// 	userDetails: () => {
					// 		return resp.data
					// 	}
					// }
					return res.render('index', {data: {endPoint: msEndpoint, currentUser: resp}})
				}
				else {
					db.collection('users').doc(resp.data.email).set({
						name: resp.data.name,
						question: 1,
						points: {},
						answers: {}, 
						reload: false,
						start_time: 0,
						time: {},
						total_points: 0
					}).then(() => {
						// module.exports = {
						// 	userDetails: () => {
						// 		return resp.data
						// 	}
						// }
						return res.render('index', {data: {endPoint: msEndpoint, currentUser: resp}})
					})
				}
			})
		}).catch((err) => console.log(err))
	}).catch((err) => {
		console.log(err.message)
	})
	
}) 

module.exports = {
	router: router,
}