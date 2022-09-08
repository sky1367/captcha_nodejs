var c_model = require('../model/model0906');
const fs = require('fs');

exports.Home = (req, res) => {
};
exports.Demo_uploadOrigin = (req, res) => {
    // console.log("CON: " + req.body)
    // console.log("req.body.filename: " + req.body.filename);
    var path = './public/img/'+ req.body.filename
    var image = req.body.file
    var data = image.split(',')[1]
    fs.writeFileSync(path, data,{encoding:'base64'}); 
    // console.log("data: " + data);

    var temp = fs.readFileSync(path); // 讀取圖片成Base64格式
    var buff        = new ArrayBuffer(temp);
    var base64data  = buff.toString('base64');
    console.log("BASE: " + base64data)
    
    // 傳送model 回傳 Base64 , 轉換 buffer ，存圖片
    c_model.Demo_uploadOrigin(base64data).then((results)=>{
        console.log("results3: " + results);
        res.json({
            msg:'success',resultFile :req.body.filename, pythonResults :results
        });
    })
};
exports.Demo_uploadNew = (req, res) => {
    var path = './public/img/'+ req.body.filename
    var image = req.body.file
    var data = image.split(',')[1]
    fs.writeFileSync(path, data,{encoding:'base64'}); 
    // console.log("data: " + data);

    var temp = fs.readFileSync(path); // 讀取圖片成Base64格式
    var buff        = new ArrayBuffer(temp);
    var base64data  = buff.toString('base64');
    console.log("BASE: " + base64data)
    
    // 傳送model 回傳 Base64 , 轉換 buffer ，存圖片
    c_model.Demo_uploadNew(base64data).then((results)=>{
        console.log("results3: " + results);
        res.json({
            msg:'success',resultFile :req.body.filename, pythonResults :results
        });
    })
};
exports.Demo_webCrawler = (req, res) => {
    if (req.body["udnVal"]) {
        c_model.Demo_webCrawler(req.body["udnVal"]).then((results)=>{
            console.log("results3: " + results);
            res.json({
                msg:'success'
            });
        }) 
    }
    else {
        c_model.Demo_webCrawler(req.body["sanminVal"]).then((results)=>{
            console.log("results4: " + results);
            res.json({
                msg:'success'
            });
        }) 
    }
     

};
exports.Demo_refSource = (req, res) => {
};
exports.Demo_members = (req, res) => {
};

// exports.upload =(req,res)=>{
//     console.log(req.body)
//     path = './public/img/'+ req.body.filename

//     var image = req.body.file
//     var data = image.split(',')[1]
//     fs.writeFileSync(path, data,{encoding:'base64'}); 


//     var temp = fs.readFileSync(path, data, {encoding: 'base64'}); // 讀取圖片成Base64格式
//     temp = JSON.stringify(temp)
    
    
//     // 傳送model 回傳 Base64 , 轉換 buffer ，存圖片
//     c_model.upload(temp).then((results)=>{
        
//         // enhancedName = `${modelUse}Enhanced_${originalName}`
//         // enhancedImagePath =`./public/enhancedImage/${enhancedName}`
//         // enhancedImageDetectPath =`./public/enhancedImageDetect/Detect_${enhancedName}`
//         // orginalImageDetectPath = `./public/uploadImageDetect/Detect_${originalName}`

//         // console.log(images["orginalImageDetect"].length)
//         // console.log(images["enhancedImage"].length)
//         // console.log(images["enhancedImageDetect"].length)

//         // const enhancedImagebuffer = Buffer.from(images["enhancedImage"], "base64");
//         // const enhancedImageDetectbuffer = Buffer.from(images["enhancedImageDetect"], "base64");
//         // const orginalImageDetectbuffer = Buffer.from(images["orginalImageDetect"], "base64");
//         // ??const buff = Buffer.from(images["path"], "base64");
        
//         // fs.writeFileSync(enhancedImagePath, enhancedImagebuffer); 
//         // fs.writeFileSync(enhancedImageDetectPath, enhancedImageDetectbuffer); 
//         // fs.writeFileSync(orginalImageDetectPath, orginalImageDetectbuffer); 
//         // ??fs.writeFileSync(path, buff); 


//         res.json({
//             msg:'success',resultFile :req.body.filename, pythonResults :results
//         });
//     })

// }