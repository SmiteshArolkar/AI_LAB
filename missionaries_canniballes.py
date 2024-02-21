from collections import deque

def isvalid(state) :
    m_left , c_left , boat , m_right , c_right = state
    if m_left < 0 or m_right < 0 or c_left < 0 or c_right < 0 :
        return False
    if  ( m_left < c_left and m_left > 0 ) or (m_right < c_right and m_right   > 0 ) :
        return False
    return True

def succesor(state) :
    succesor_list = []
    m_left , c_left ,boat , m_right , c_right = state
    
    if boat == 1 : 
        #move to right
        # for i in range(1,3) :
        #     for j in  range(3) :
        #         new_state = (m_left - i,c_left - j ,0,m_right + i ,c_right +j)
        #         if( isvalid(new_state) ) :
        #             succesor_list.append(new_state)
        if m_left == 1 and c_left == 1 :
            new_state = (m_left-1,c_left,0,m_right+1,c_right)
            if(isvalid(new_state)) :
                succesor_list.append(new_state)
        
        
    else :
        for i in range (1,3):
            for j in range(3) :
                if 0 < i+j <=2 :
                    new_state = (m_left+i,c_left+j,1,m_right-i,c_right-j)
                    if(isvalid(new_state)) :
                        succesor_list.append(new_state)
                    
    return succesor_list

def missionaries_cannibals(start,goal) :
    visited = set()
    queue = deque([(start,[])])
    result = []
    
    while queue :
        current_state,current_path = queue.popleft()
 
        
        if current_state == goal :
            result.append(current_path + [current_state])
        
        if current_state not in visited :
            visited.add(current_state)
            for new_state in succesor(current_state) :
                queue.append((new_state,current_path + [current_state]))
               
        
    
    return result
    


start = (3,3,1,0,0)
goal = (0,0,0,3,3)

result = missionaries_cannibals(start,goal)
for i in result :
    print(i)