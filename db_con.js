const mysql = require("mysql")

const db_con = mysql.createConnection({
    host: "localhost",
    port: 3307,
    user: "root",
    password: "",
    database: "barkbutlers"
});

db_con.connect(err => {
    if (err) {
        console.log("Database connection failed!", err);
        exit();
    }
    
    console.log("Connected to database");
    db_con.query("SELECT * FROM person", (err, result, fields) => {
        if (err) throw err
        console.log(result);
    })
});