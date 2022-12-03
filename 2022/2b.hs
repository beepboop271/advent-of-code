value :: Char -> Integer
value 'A' = 1
value 'B' = 2
value 'C' = 3
value _ = error ""

value2 :: Char -> Integer
value2 'X' = 0
value2 'Y' = 3
value2 'Z' = 6
value2 _ = error ""

outcome :: Char -> Char -> Char
outcome them 'Y' = them
outcome 'A' path = if path == 'Z' then 'B' else 'C'
outcome 'B' path = if path == 'Z' then 'C' else 'A'
outcome 'C' path = if path == 'Z' then 'A' else 'B'

score :: Char -> Char -> Integer
score them us = value2 us + value (outcome them us)

process :: [(Char, Char)] -> Integer
process = sum . map (uncurry score)

splitMoves :: String -> (Char, Char)
splitMoves [them, _, us] = (them, us)
splitMoves x = error x

processInput :: [String] -> [String]
processInput inp = [(show . process . map splitMoves) inp]

main = interact (unlines . processInput . lines)
