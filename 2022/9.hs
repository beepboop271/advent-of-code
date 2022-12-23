import Data.List (foldl')
import Data.Set (Set, insert, size, fromList)
import Text.Printf (printf)

type Point = (Int, Int)
type Rope = [Point]
type Visited = Set Point

distSquared :: Point -> Point -> Int
distSquared (x1, y1) (x2, y2) = (x2 - x1)^2 + (y2 - y1)^2

findStep :: Point -> Point -> Point
findStep head@(hx, hy) next@(nx, ny)
  | distSquared head next <= 2 = (0, 0)
  | dx == 0          = (0, stepY)
  | dy == 0          = (stepX, 0)
  | abs dx == 1      = (dx, stepY)
  | abs dy == 1      = (stepX, dy)
  | abs dx == abs dy = (stepX, stepY)
  | otherwise        = error (show dx ++ " " ++ show dy)
  where
    stepX = quot dx (abs dx)
    stepY = quot dy (abs dy)
    dx = hx - nx
    dy = hy - ny

stepSingle :: Point -> Visited -> Rope -> (Visited, Rope)
stepSingle (0, 0) v rope = (v, rope)
stepSingle (dx, dy) v ((hx, hy):rest) = case rest of
  []     -> (insert head' v, [head'])
  next:_ -> let (v', rest') = stepSingle (findStep head' next) v rest
            in (v', head':rest')
  where
    head' = (hx+dx, hy+dy)

stepN :: Visited -> Rope -> (Int, Int, Int) -> (Visited, Rope)
stepN v r (dx, dy, n) = iterate (uncurry (stepSingle (dx, dy))) (v, r) !! n

parse :: String -> (Int, Int, Int)
parse (d:' ':num) = case d of
  'L' -> (-1, 0, amount)
  'R' -> (1, 0, amount)
  'U' -> (0, 1, amount)
  'D' -> (0, -1, amount)
  where
    amount = read num
parse _ = error ""

processInput :: Int -> [String] -> String
processInput length = show
  . size
  . fst
  . foldl' (uncurry stepN) (fromList [(0, 0)], replicate length (0, 0))
  . map parse

main = interact (
    (\ inp -> printf "A: %s\nB: %s\n" (processInput 2 inp) (processInput 10 inp))
    . lines
  )
