const express = require("express");
const productController = require("../controllers/Product.controller");
const userController = require("../controllers/User.controller");

// Multer configuration
const multer = require("multer");
const storageConfig = multer.diskStorage({
    destination: (req, res, cb) => {
        cb(null, "./uploads");
    },
    filename: (req, file, cb) => {
        cb(null, file.fieldname + "_" + Date.now() + "_" + file.originalname);
    }
});

const upload = multer({ storage: storageConfig });

// Product routes
const router = express.Router();
router.get("/products", productController.getAll);
router.get("/products/:code", productController.getByCode);
router.post("/products", upload.single("image"), productController.create);
router.put("/products/:code", productController.update);
router.delete("/products/:code", productController.delete);
router.patch("/products/:code/image", upload.single("image"), productController.changeProductImage);

// rutas de usuario
router.post("/users", userController.insert);
router.post("/authenticate", userController.validateUser);

module.exports = router;
