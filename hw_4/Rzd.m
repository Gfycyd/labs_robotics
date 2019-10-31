function [Rzd] = Rzd(t)
    Rzd = [-sin(t) -cos(t) 0 0; cos(t) -sin(t) 0 0; 0 0 0 0; 0 0 0 0];
end