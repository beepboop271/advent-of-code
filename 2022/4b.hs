import Data.Char (isDigit)

overlap :: (Int, Int, Int, Int) -> Bool
overlap (e1s, e1e, e2s, e2e)
  | e1s <= e2e && e1e >= e2s = True
  | e2s <= e1e && e2e >= e1s = True
  | otherwise = False

extractInts :: String -> (Int, Int, Int, Int)
extractInts s = (read e1s, read e1e, read e2s, read e2e)
  where (e2e, _) = span isDigit rest1
        (e2s, _:rest1) = span isDigit rest2
        (e1e, _:rest2) = span isDigit rest3
        (e1s, _:rest3) = span isDigit s

processInput :: [String] -> String
processInput = show . length . filter overlap . map extractInts

main = interact ((++ "\n") . processInput . lines)
