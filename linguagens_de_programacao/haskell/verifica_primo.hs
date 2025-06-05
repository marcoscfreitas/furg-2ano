main :: IO ()
main = do
    putStrLn "digite um número:"
    input <- getLine
    let n = read input :: Integer

    if n <= 0 then
        putStrLn "erro: digite um número válido."
    else do
        if ehPrimo n then
            putStrLn (show n ++ " é um número primo.")
        else
            putStrLn (show n ++ " não é um número primo.")

ehPrimo :: Integer -> Bool
ehPrimo 1 = False
ehPrimo 2 = True
ehPrimo n = not (any (\x -> n `mod` x == 0) [2..(floor . sqrt $ fromIntegral n)])
