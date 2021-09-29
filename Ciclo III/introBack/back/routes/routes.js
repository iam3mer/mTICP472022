const express = require("express");
const restaurantsController = require("../controller/RestaurantsController");

const router = express.Router();

// Rutes Restaurants
router.get("/restaurants/all", restaurantsController.getAll);
router.get("/restaurants/:id", restaurantsController.getById);
router.get("/restaurants/:param1/:param2", restaurantsController.getP12);
router.delete("/restaurants/:id", restaurantsController.deleteById);
router.post("/restaurants/", restaurantsController.create);
router.put("/restaurants/:id/:val", restaurantsController.updateById);
router.put("restaurants/:id", restaurantsController.replaceById);

module.exports = router;
