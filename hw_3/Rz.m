function [Rz] = Rz(t)
    Rz = [cos(t) -sin(t) 0 0; sin(t) cos(t) 0 0; 0 0 1 0; 0 0 0 1]
end