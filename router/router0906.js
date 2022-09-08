var express = require('express');
var router = express.Router();
const multer = require('multer');

const upload = multer({dest:"uploads"});
var c_controller = require("../controller/controller0906");


router.all("/Home", c_controller.Home);
// router.post("/Demo_uploadOrigin", c_controller.Demo_uploadOrigin);
router.all("/Home/Demo_uploadOrigin", c_controller.Demo_uploadOrigin);
router.all("/Home/Demo_uploadNew", c_controller.Demo_uploadNew);
router.all("/Home/Demo_webCrawler", c_controller.Demo_webCrawler);
router.all("/Home/Demo_refSource", c_controller.Demo_refSource);
router.all("/Home/Demo_members", c_controller.Demo_members);

module.exports = router;
