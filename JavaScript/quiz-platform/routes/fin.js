const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    const userEnd = require('./play');
    try {
        let placeFin = userEnd.userFin();
        res.render('fin');
    }
    catch {
        console.log('User hasn\'t ended yet');
        res.redirect('./play')
    }
})

module.exports = router;