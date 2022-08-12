import {Component, ReactElement } from 'react';
import dictionary from '../dict.json';
/*
const withDictionary = (WrappedComponent: ReactElement, data: {[key:string]:string}) => {
    class HOC extends Component {
        render(){
            return <WrappedComponent {...this.props}/>
        }
    };
    return HOC;
};

export const getStaticProps = async () => {
    return dictionary
};
  
export default withDictionary;*/