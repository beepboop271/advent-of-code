import Data.List (foldl')
import Data.Map.Strict (Map, alter, empty, size)
import Data.Sequence (Seq ((:<|)), fromList, (|>))

addCounter :: Maybe Int -> Maybe Int
addCounter (Just i) = Just (i+1)
addCounter Nothing = Just 1

removeCounter :: Maybe Int -> Maybe Int
removeCounter (Just i)
  | i > 1 = Just (i-1)
  | otherwise = Nothing
removeCounter Nothing = Nothing

-- count number of occurrences of a char in a string
-- if a count is zero, it is removed from the counter
initMap :: String -> Map Char Int
initMap = foldl' (flip (alter addCounter)) empty

-- abcdefghijk
--    ^--^      sliding window of length n
-- back  front
findDistinctRunHelper :: Int -> Int -> String -> Seq Char -> Map Char Int -> Int
findDistinctRunHelper n idx (front:s) (back:<|window) m
  | size m == n = idx
  | otherwise = findDistinctRunHelper n (idx+1) s newWindow newM
  where newM = alter removeCounter back (alter addCounter front m)
        newWindow = window |> front
findDistinctRunHelper _ idx _ _ _ = error (show idx)

findDistinctRun :: Int -> String -> Int
findDistinctRun n s = findDistinctRunHelper n n tail (fromList head) (initMap head)
  where (head, tail) = splitAt n s

main = do
  line <- getLine
  putStr "A: "
  print (findDistinctRun 4 line)
  putStr "B: "
  print (findDistinctRun 14 line)
