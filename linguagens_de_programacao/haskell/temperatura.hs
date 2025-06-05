main :: IO ()
main = do
    putStrLn "digite a temperatura em fahrenheit:"
    input <- getLine
    let f = read input :: Double
    let c = fahrenheitParaCelsius f
    putStrLn $ "temperatura em celsius: " ++ showFFloat 2 c

fahrenheitParaCelsius :: Double -> Double
fahrenheitParaCelsius f = ((f - 32) * 5) / 9
showFFloat :: Int -> Double -> String
showFFloat n x = show (fromIntegral (round (x * factor)) / factor)
    where factor = 10 ^ n
