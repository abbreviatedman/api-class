window.addEventListener("load", () => {
  const directives = getAllDirectives();
  directives.forEach(handleDirective);
  document.querySelectorAll(".slides").forEach((slide) => {
    // slide.style.marginTop = "80px";
    // slide.style.marginLeft = "120px";
    // slide.style.padding = "0px";
  });

  // document.querySelectorAll(".reveal").forEach((slide) => {
  //   slide.classList.toggle('default')
  // })
});

// Gets all styling directives in deck.
const getAllDirectives = () => {
  const slides = Array.from(document.querySelectorAll(".slides section"));
  const elements = slides.reduce(
    (elements, slide) => [...elements, ...slide.childNodes],
    []
  );

  return elements
    .filter((element) => element.nodeType === Node.COMMENT_NODE)
    .map((directive) => ({
      slide: directive.parentNode,
      directive: directive.nodeValue.trim(),
    }));
};

const handleDirective = ({ slide, directive }) => {
  switch (directive) {
    case "incremental-list":
      makeListItemsIncremental(slide);
      break;

    case "splash-page":
      makeSplashPage(slide);

      break;

    case "ending-splash-page":
      makeEndingSplashPage(slide);

      break;

    // TODO
    case "incremental-item":
      break;

    // TODO
    case "center":
      break;

    default:
      break;
  }
};

const makeListItemsIncremental = (slide) =>
  slide
    .querySelectorAll("li")
    .forEach((listItem) => listItem.classList.add("fragment"));

const makeSplashPage = (slide) => {
  slide.classList.add("splash-page");
  slide.style.marginLeft = "-200px";
  // add splash-page class to background div as well
  document.querySelectorAll("section").forEach((candidate, i) => {
    if (candidate === slide) {
      document
        .querySelector(".backgrounds")
        .childNodes[i].classList.add("splash-page");
    }
  });
};

const makeEndingSplashPage = (slide) => {
  slide.classList.add("ending-splash-page");
  slide.style.marginLeft = "-200px";
  // add splash-page class to background div as well
  document.querySelectorAll("section").forEach((candidate, i) => {
    if (candidate === slide) {
      document
        .querySelector(".backgrounds")
        .childNodes[i].classList.add("ending-splash-page");
    }
  });
};
