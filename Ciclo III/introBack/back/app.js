require("dotenv").config();

const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({extended: true}))

// rutas
app.use("/api",require("./routes/routes"));

// DB
const mongoose = require("mongoose");
mongoose.connect(process.env.URI_DB)
  .then(() => console.log("Conexión OK con DB"))
  .catch(err => console.error(err));

const port = process.env.PORT;
app.listen(port, () => 
  console.log(`La aplicación esta escuchando en http://localhost:${port}`)
)
