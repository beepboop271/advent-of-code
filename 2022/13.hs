import Data.Char (isDigit)
import Data.List (findIndices, sort)
import Data.Maybe (fromJust, mapMaybe, isJust)
import Data.Text (Text, lines, pack, splitOn, unpack)
import Text.Printf (printf)

data Packet = I Int | L [Packet]

instance Eq Packet where (==) p1 p2 = compare p1 p2 == EQ

instance Ord Packet where compare = cmpPacket

cmpPacket :: Packet -> Packet -> Ordering
cmpPacket (I left) (I right) = compare left right
cmpPacket (L []) (L []) = EQ
cmpPacket (L []) (L right) = LT
cmpPacket (L left) (L []) = GT
cmpPacket (L (headL:restL)) (L (headR:restR)) =
  case cmpPacket headL headR of
    EQ  -> cmpPacket (L restL) (L restR)
    ord -> ord
cmpPacket left@(L _) right@(I _) = cmpPacket left (L [right])
cmpPacket left@(I _) right@(L _) = cmpPacket (L [left]) right

parse :: String -> (Maybe Packet, String)
parse [] = (Nothing, [])
parse (',':rest) = parse rest
parse (']':rest) = (Nothing, rest)
parse ('[':rest) = (Just (L packets), snd after)
  where
    parses = iterate (parse . snd) (parse rest)
    (scanList, after:_) = span (isJust . fst) parses
    packets = mapMaybe fst scanList
parse s@(c:rest)
  | isDigit c =
    let (n, after) = span isDigit s
    in (Just (I (read n)), after)
  | otherwise = error "parse error (illegal char)"

parseTwo :: Text -> (Packet, Packet)
parseTwo str =
  case Data.Text.lines str of
    [left, right] -> (doParse left, doParse right)
    _             -> error "parse error (line count)"
  where doParse = fromJust . fst . parse . unpack

findValidPairIdxs :: [(Packet, Packet)] -> [Int]
findValidPairIdxs = map fst . filter (uncurry (<) . snd) . zip [1..]

processInputA :: Text -> Int
processInputA = sum . findValidPairIdxs . map parseTwo . splitOn (pack "\n\n")

findMarkerIdxs :: [Packet] -> Int
findMarkerIdxs = product . map (+ 1) . findIndices
  (\x -> x == L [L [I 2]] || x == L [L [I 6]])

processInputB :: String -> Int
processInputB = findMarkerIdxs
  . sort
  . (L [L [I 2]]:)
  . (L [L [I 6]]:)
  . map (fromJust . fst . parse)
  . filter (not . null)
  . Prelude.lines

main = interact (\s ->
    printf "A: %d\nB: %d\n" (processInputA (pack s)) (processInputB s)
  )
