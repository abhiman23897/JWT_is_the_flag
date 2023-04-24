import React from 'react';
import { Navigate } from 'react-router-dom';
import { isExpired } from 'react-jwt';

const RouteGuard = ({ children }) => {
    function verifyJWT() {
        let flag = false;

        //check user has JWT token
        localStorage.getItem("token") ? flag=true : flag=false
        
        if(flag){
            //check if JWT token is valid
            const isExpiredToken = isExpired(localStorage.getItem("token"));
            isExpiredToken ? flag=false : flag=true;
        }
        return flag
    }

    if(verifyJWT()){
        return children;
    }
    else{
        alert("Invalid JWT token"); 
        return <Navigate to="/" />;
    }
};

export default RouteGuard;