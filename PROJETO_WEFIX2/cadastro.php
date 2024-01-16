<?php
    include("config_ban.php");

    $modelo = $_POST['modelo'];
    $quantidade=$_POST['$quantidade'];
    $custo=$_POST['custo'];
    $lojista=$_POST['lojista'];
    $cliente=$_POST['cliente'];

    $sql="INSERT INTO estoque_wefix(modelo,quantidade,custo,lojista,cliente) 
    VALUES ('$modelo', $quantidade,$custo,$lojista,$cliente)";

    if(mysqli_query($conexao, $sql)){
        echo "Cadastrado com sucesso";
    }
    else{
        echo " Deu um erro";
    }
mysqli_close($conexao);
?>
