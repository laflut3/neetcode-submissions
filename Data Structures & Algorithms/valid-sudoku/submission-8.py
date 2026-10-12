class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, len(board)):
            column: List[str] = []
            
            for j in range(0, len(board[i])):
                if not self.validNumberNotRepeat(board[i]):
                    return False
                column.append(board[j][i])
            
            if not self.validNumberNotRepeat(column): 
                return False

        for rowBegin in range(0,9,3):
            for columnBegin in range(0,9,3):
                square = [
                    board[row][column]
                    for row in range(rowBegin, rowBegin + 3)
                    for column in range(columnBegin, columnBegin + 3)
                ]
                
                if not self.validNumberNotRepeat(square): 
                    return False
                
        return True
    
    def validNumberNotRepeat(self, line: List[str]) -> bool:
        count: Dict = {}
        for value in line:
            if value == '.':
                continue

            count[value] = count.get(value, 0) +1
            if count[value] > 1:
                return False
        
        return True