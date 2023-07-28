#include <string>
#include <vector>
#include <sstream>

using namespace std;

string likes(const vector<string> &names)
{
  
  vector<string>::const_iterator it = names.begin();
  
  ostringstream stream;
  
  if(names.size() == 0)
    stream << "no one";
  
  else
  {
    stream << (*it);
    
    if(names.size() > 1)
    {
      if(names.size() > 2)
      {
        ++it;
        stream << ", " << (*it);
      }
      
      stream << " and ";
      if(names.size() <= 3)
      {
        ++it;
        stream << (*it);
      }
        
      else
        stream << distance(it, names.end() - 1) << " others";
    }
  }
 

  
  stream << " like" << (names.size() > 1 ? "" : "s")
         << " this";
  
    
  return stream.str();
}