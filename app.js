const express = require('express')
const app = express()

app.listen(3000, () => {
console.log('server running on port 3000')
})

var cartrouter = require('./router/router0906');

app.set('view engine','ejs');
app.use(express.json({limit: '50mb', extended: true}));
app.use(express.urlencoded({limit: "50mb", extended: true, parameterLimit:50000}));
// app.use(express.static(__dirname));
app.use(express.static(__dirname + '/public/'));
app.use('/index',cartrouter);

app.get('/',(req,res)=>{
  res.render('./Home')
})
app.get('/Home/Demo_uploadOrigin',(req,res)=>{
  res.render('./Demo_uploadOrigin')
})
app.get('/Home/Demo_uploadNew',(req,res)=>{
  res.render('./Demo_uploadNew')
})
app.get('/Home/Demo_webCrawler',(req,res)=>{
  res.render('./Demo_webCrawler')
})
app.get('/Home/Demo_refSource',(req,res)=>{
  res.render('./Demo_refSource')
})
app.get('/Home/Demo_members',(req,res)=>{
  res.render('./Demo_members')
})
