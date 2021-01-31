const express = require('express')
const bodyParser = require('body-parser');
const cors = require('cors');
const { raw } = require('body-parser');

const app = express();
const port = 3000;

// Where we will keep books
let books = [];

app.use(cors());

// Configuring body parser middleware
app.use(bodyParser.urlencoded({
    extended: false
}));
app.use(bodyParser.json());

app.post('/data', (req, res) => {
    const data = req.body;
    let parameter = '';
    const readParameter = Object.values(data)
    for (let i = 0; i < readParameter.length - 1; i++) {
        parameter += readParameter[i] + ' ';
    }
    parameter += readParameter[readParameter.length - 1];
    console.log(parameter);
    const exec = require('child_process').exec;
    const execSync = require('child_process').execSync;
    // 异步执行
    let pyParemeter = 'python3 Hack_Py_Script.py ' + parameter
    let rawData;
    exec(pyParemeter, function (error, stdout, stderr) {
        if (error) {
            console.info('stderr : ' + stderr);
        }
        rawData = JSON.parse(stdout);
         res.send(rawData);
    })
    // 同步执行
    // const output = execSync('python web.py')
    // console.log('sync: ' + output.toString())
    // console.log('over')
    console.log(rawData);
  
});

app.listen(port, () => console.log(`Hello world app listening on port ${port}!`));