// const request = require('request');
var { PythonShell } = require('python-shell')


exports.Home = () => {
};
var results;
exports.Demo_uploadOrigin = async (base64data) =>{
    // console.log("MOD:")
    // console.log("MOD2:" + base64data)
    let promise = new Promise (function (resolve, reject) {
        PythonShell.run('./originModel.py', null, async function(err, data) {
            if (err) throw err;
            // console.log("data: " + data);
            var results = await JSON.stringify(data)
            // console.log("results: " + results);
            // console.log("type of results: " + typeof(results));
            var results = await results.slice(-7,-2)
            console.log("results2: " + results);
            console.log("type of results2: " + typeof(results));
            if (err) reject (err);
            else resolve(results);
            })
    }); 
    console.log("promise: " + promise)
    return promise;
};
exports.Demo_uploadNew = () => {
    let promise = new Promise (function (resolve, reject) {
        PythonShell.run('./newModel.py', null, async function(err, data) {
            if (err) throw err;
            // console.log("data: " + data);
            var results = await JSON.stringify(data)
            // console.log("results: " + results);
            // console.log("type of results: " + typeof(results));
            var results = await results.slice(-7,-2)
            console.log("results2: " + results);
            console.log("type of results2: " + typeof(results));
            if (err) reject (err);
            else resolve(results);
            })
    }); 
    console.log("promise: " + promise)
    return promise;
};
exports.Demo_webCrawler = (data) => {
    console.log("--------------" + data)
    if (data == "聯合知識庫"){
        pFile = './udn.py'
    }
    else {
        pFile = './sanmin.py'
    }
    console.log("pFile000" + pFile)
    let promise = new Promise (function (resolve, reject) {
        console.log("pFile" + pFile)
        PythonShell.run(pFile, null, async function(err, data) {
        if (err) throw err;
        var results = await JSON.stringify(data)
        console.log("results: " + results);
        // res.json({msg:'success'});
        });
    }); 
    console.log("promise: " + promise)
    return promise;
    
    // let promise = new Promise (function (resolve, reject) {
    //     console.log("++++++" + data)
    //     if (data = "聯合知識庫"){
    //         PythonShell.run('./udn.py', null, async function(err, data) {
    //         if (err) throw err;
    //         var results = await JSON.stringify(data)
    //         console.log("results: " + results);
    //         // res.json({msg:'success'});
    //         });
    //     }
    //     else {
    //         PythonShell.run('./sanmin.py', null, async function(err, data) {
    //         if (err) throw err;
    //         var results = await JSON.stringify(data)
    //         console.log("results: " + results);
    //         // res.json({msg:'success'});
    //         });
    //     }

    // }); 

};
exports.Demo_refSource = () => {
};
exports.Demo_members = () => {
};



// exports.upload = async (temp) =>{

//   var buff        = new ArrayBuffer(temp);
//   var base64data  = buff.toString('base64');
  
//   if (req.body && req.body.filename) {
//     if (/\.(jpg|jpeg|png|gif)$/i.test(req.body.filename)) {
//         PythonShell.run('./originModel.py', null, async function(err, data) {
//             if (err) throw err;
//             console.log("data: " + data);
//             var results = await JSON.stringify(data)
//             console.log("results: " + results);
//             console.log("type of results: " + typeof(results));
//             var results = results.slice(-7,-2)
//             console.log("results2: " + results);
//             console.log("type of results2: " + typeof(results));
//             // console.log("results[0] type:" + typeof(results[0]));
//             // 回傳string
//             // res.json({msg:'success',resultFile :req.body.filename, pythonResults :results});
//             return results
//         });
//     }
// }

// //   images = {
// //     "orginalImageDetect":orginalImageDetect,
// //     "enhancedImage":enhancedImage,
// //     "enhancedImageDetect":enhancedImageDetect,
// //   }
//   // console.log(images["orginalImageDetect"].length)
//   // console.log(images["enhancedImage"].length)
//   // console.log(images["enhancedImageDetect"].length)
// //   return images
// }