import { Helmet } from "react-helmet";

function Home() {
  return (
    <>
      <Helmet>
        <meta charSet="utf-8" />
        <title>Amit Prafull.com</title>
        <meta name="description" content="Amitprafull.com site description in short - This would be my site for running online courses" />
        <link rel="canonical" href="http://mysite.com/example" />
      </Helmet>
      <section className="heading">
        <h1>Home Page of React And Fast API</h1>
      </section>
    </>
  );
}

export default Home;
