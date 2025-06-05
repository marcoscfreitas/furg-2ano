main :: IO ()
main = do
    putStrLn "digite o valor de x:"
    inputX <- getLine
    putStrLn "digite o valor de n:"
    inputN <- getLine

    let x = read inputX :: Integer
    let n = read inputN :: Integer

    if n < 0 then
        putStrLn "erro: insira um número válido."
    else do
        let resultado = potencia x n
        putStrLn ("resultado de " ++ show x ++ "^" ++ show n ++ " = " ++ show resultado)

potencia :: Integer -> Integer -> Integer
potencia _ 0 = 1
potencia x n = x * potencia x (n - 1)
