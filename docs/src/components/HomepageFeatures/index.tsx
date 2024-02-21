import clsx from 'clsx';

import Heading from '@theme/Heading';

import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  // Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: JSX.Element;
};

// Easily integrate Nebuly's SDK with your favorite programming language and begin analyzing user data within minutes.

const FeatureList: FeatureItem[] = [
  {
    title: 'Easy to Use',
    description: (
      <>xLeap's SDK is designed to be easily integrated within your project in your favorite programming language.</>
    ),
  },
  {
    title: 'Focus on What Matters',
    description: <>xLeap help you in analyzing user data within minutes, and lets you focus on what matters.</>,
  },
  {
    title: 'Insightful dashboard',
    description: (
      <>
        xLeap's dashboard lets' you add view all LLM data, and add trigger to get notifications of critical edge cases.
      </>
    ),
  },
];

function Feature({ title, description }: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className='text--center padding-horiz--md'>
        <Heading as='h3'>{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className='container'>
        <div className='row'>
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
