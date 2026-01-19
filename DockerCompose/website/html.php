<html>
    <head>
        <title>My Shop</title>
    </head>
    <body>
        <h1>La liste des produits disponibles est :</h1>
        <ul>
            <?php
            // Récupération du JSON depuis le service "product-service"
            // On utilise le port 80 car c'est le port exposé DANS le réseau Docker
            $json = file_get_contents('http://product-service/');

            // Décodage du JSON en objet PHP
            $obj = json_decode($json);

            // Récupération du tableau de produits
            $products = $obj->products;

            // Boucle d'affichage des produits sous forme de <li>
            foreach ($products as $product) {
                echo "<li>$product</li>";
            }
            ?>
        </ul>
    </body>
</html>
