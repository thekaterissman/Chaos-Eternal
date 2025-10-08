declare namespace hz {
  class Component<T> {
    props: any;
    entity: Entity;
  }

  const PropTypes: {
    Entity: any;
  };

  class TextGizmo {
    text: string;
  }

  class Entity {
    as<T>(type: new () => T): T;
  }

  function registerComponent(component: any): void;
}

declare module "horizon/core" {
  export = hz;
}