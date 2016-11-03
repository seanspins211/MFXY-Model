function s = sumUp(q,N0)
    A = repmat(q,N0,1);
    AT  = A';
    sines = sin(AT - A);
    s = sum(sines,2);
    s = s';
end

%deals with summing the sine terms in the Hamiltonian