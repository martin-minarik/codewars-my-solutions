std::vector<int> solve(std::string s){
    std::vector<int> result {0, 0, 0, 0};
    for(auto &chr: s)
    {
      if((chr >= 'A') && (chr <= 'Z'))
        ++result[0];
        
      else if((chr >= 'a') && (chr <= 'z'))
        ++result[1];
        
      else if((chr >= '0') && (chr <= '9'))
        ++result[2];
      
      else
        ++result[3];
      
    }
      
    return result;
}