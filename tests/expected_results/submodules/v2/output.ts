/* tslint:disable */
/* eslint-disable */
/**
/* This file was automatically generated from pydantic models by running pydantic2ts.
/* Do not modify it by hand - just update the pydantic models and then re-run the script
*/

export interface AnimalShelter {
  address: string;
  cats: Cat[];
  dogs: Dog[];
}
export interface Cat {
  name: string;
  age: number;
  declawed: boolean;
  breed: CatBreed;
}
export interface Dog {
  name: string;
  age: number;
  breed: DogBreed;
}

export const enum CatBreed {
  domestic_shorthair = "domestic shorthair",
  bengal = "bengal",
  persian = "persian",
  siamese = "siamese"
}
export const enum DogBreed {
  mutt = "mutt",
  labrador = "labrador",
  golden_retriever = "golden retriever"
}
