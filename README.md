# Timeless Jewel Trade Search
Searches for timeless jewels with given values on Path of Exile's trade site.

## How to use
1. Optional: Enter authenticated PoE session ID (for instructions on finding it, see here: http://www.vhpg.com/how-to-find-poe-session-id/)
2. Select which type of jewel you'd like to search for
3. Select which names for the jewel you're looking for
4. Type the jewel seed values you're looking for, separated by commas (no spaces)
5. Select the realm and league you're searching in

![image](https://user-images.githubusercontent.com/62523675/185701778-aaef572d-49cc-4477-9574-261229b76379.png)

6. Click "Search" and the trade will be opened in a new browser tab

![image](https://user-images.githubusercontent.com/62523675/185701829-820d6bca-e4d2-48b2-9473-bff84fc818af.png)

Note that if you don't provide an authenticated PoE session ID there is a much lower tolerance with regards to search complexity, going from 188 maximum search terms down to 38. This means 38 seeds with one name selected, 19 with two selected, and only 12 with all three selected. If this means you'll need to do multiple searches I'd recommend splitting the searches by name before IDs, since it's easier to switch the name you're looking for as opposed to changing dozens of numbers.

For example, if you're looking for any of 24 different values but don't care which name the jewel has, you could either:
- Search for all 24 seeds for name 1, then name 2, then name 3
- Search for the first 12 seeds with all 3 names, then search for the other 12 seeds
