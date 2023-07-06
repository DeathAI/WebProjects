const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const fs = require('fs');
const compiler = require('compilex');

const app = express();
app.use(cookieParser());

compiler.init({
  stats: true
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname,"index.html"));
});

app.get('/exePyCode', (req, res) => {
  res.sendFile(path.join(__dirname,"PyCode.html"));
});


app.post('/exePyCode', (req, res) => {
  EncodedCode = req.cookies.code;
  codeArr = JSON.parse(decodeURIComponent(EncodedCode));
  code = "";
  for(let i=0;i<codeArr.length;i++){
    code = code+codeArr[i]+"\n";
  }
  console.log(code);
  let envData = { OS : "windows"};
  compiler.compilePython( envData , code , function(data){
    const html = fs.readFileSync(path.join(__dirname,"PyCode.html"), 'utf8');
    let tmp = String(data).split('\n');
    op = ""
    for(let i=0;i<tmp.length;i++){
      op = op+tmp[i]+'<br>';
    }
    res.send(html+op);
  });
});



app.get('/exeCppCode', (req, res) => {
  res.sendFile(path.join(__dirname,"CppCode.html"));
});


app.post('/exeCppCode', (req, res) => {
  EncodedCode = req.cookies.code;
  codeArr = JSON.parse(decodeURIComponent(EncodedCode));
  code = "";
  for(let i=0;i<codeArr.length;i++){
    code = code+codeArr[i]+"\n";
  }
  console.log(code);

  let envData = { OS : "linux" , cmd : "gcc"};
  compiler.compileCPP( envData , code , function(data){
    const html = fs.readFileSync(path.join(__dirname,"CppCode.html"), 'utf8');
    let tmp = String(data).split('\n');
    op = "";
    for(let i=0;i<tmp.length;i++){
      op = op+tmp[i]+'<br>';
    }
    res.send(html+op);
  });
});

app.listen(5000);

compiler.flush(function() {
  console.log('Temp file deleted successfully');
});
