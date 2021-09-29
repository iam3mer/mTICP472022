const restaurantsModel = require("../model/RestaurantsModel")

module.exports = class RestaurantsController {
  static async getAll(request, response) {
    try {
      const result = await restaurantsModel.find();
      response.status(200).json(result);
    } catch (err) {
      response.status(404).json({message: err.message});
    }
  }

  static async getById(request, response) {
    try {
      const id = request.params.id;
      const result = await restaurantsModel.findOne({_id: id});
      if (result != null) {
        response.status(200).json(result)
      } else {
        response.status(404).json();
      }
    } catch (err) {
      response.status(400).json({message: err.message})
    }
  }

  static async getP12(request, response){
    try {
      const p1 = request.params.param1;
      const p2 = request.params.param2;
      const result = await restaurantsModel.find({borough: p1, cuisine:p2})
      if (result != null) {
        response.status(200).json(result)
      } else {
        response.status(404).json();
      }
    } catch (err) {
      response.status(400).json({message: err.message});
    }
  }

  static async deleteById(request, response){
    try {
      const id = request.params.id;
      await restaurantsModel.deleteOne({_id: id});
      response.status(200).json();
    } catch (err) {
      response.status(400).json({message: err.message})
    }
  }

  static async create(request, response){
    try {
      const document = request.body;
      const newRestaurant = await restaurantsModel.create(document);
      response.status(201).json(newRestaurant);
    } catch (err) {
      response.status(400).json({message: err.message})
    }
  }

  static async updateById(request, response) {
    try {
      const id = request.params.id;
      const val = request.params.val;
      const document = request.body;
      await restaurantsModel.updateOne({"_id": id}, {$set: {"borough": val}});
      response.status(200).json();
    } catch (err) {
      response.status(400).json({message: err.message})
    }
  }

  static async replaceById(request, response) {
    try {
      const id = request.params.id;
      const document = request.body;
      await restaurantsModel.update({"_id": id}, document);
      response.status(200).json();
    } catch (err) {
      response.status(400).json({message: err.message})
    }
  }
}