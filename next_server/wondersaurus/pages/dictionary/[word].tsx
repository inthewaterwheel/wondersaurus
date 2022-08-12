import { NextPage } from 'next';
import { GetStaticPaths, GetStaticProps } from 'next'
import dictionary from '../../dict.json';
import { ParsedUrlQuery } from 'querystring'

interface IParams extends ParsedUrlQuery {
    word: string
}

interface WordPageProps {
    html: string;
}

export const getStaticPaths: GetStaticPaths = async () =>  {
    const dict = dictionary as Record<string, string>;;

    const paths = Object.keys(dict).map(w => ({
        params: { word: w } 
    }))

    console.log("Saving paths: ", paths)

    return {
      paths: paths,
      fallback: false, // can also be true or 'blocking'
    }
  }

export const getStaticProps: GetStaticProps = async (context) => {
    const dict = dictionary as Record<string, string>;
    const { word } = context.params as IParams 

    console.log("Looking for word: ", word)
  return {
    props: {
      html: dict[word],
    },
  };
}

const Page: NextPage<WordPageProps> = ({html}) => {
    return (
        <div dangerouslySetInnerHTML={{__html: html}}/>
    );
}

export default Page