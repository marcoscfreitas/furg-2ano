main :: IO ()
main = do
    putStrLn "digite um número:"
    input <- getLine
    let n = read input :: Int

    if n <= 0 then
        putStrLn "erro: o número deve ser positivo."
    else do
        let impares = take n [1,3..]
        putStrLn ("os " ++ show n ++ " primeiros números ímpares são:")
        print impares