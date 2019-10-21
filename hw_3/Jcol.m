function [J] = Jcol(T)

J = [T(1:3,4);
      T(3,2);
      T(1,3);
      T(2,1)];

end