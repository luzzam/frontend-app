// types.ts
export type AppSettings = {
  apiEndpoint: string;
  appName: string;
  apiTimeout: number;
};

export type User = {
  id: number;
  name: string;
  email: string;
};

export type Product = {
  id: number;
  name: string;
  description: string;
  price: number;
};

export type Order = {
  id: number;
  userId: number;
  productId: number;
  quantity: number;
  totalPrice: number;
};

export type ProductVariant = {
  id: number;
  productId: number;
  variantName: string;
  price: number;
};

export type OrderItem = {
  id: number;
  orderId: number;
  productId: number;
  variantId: number;
  quantity: number;
  totalPrice: number;
};

export type CartItem = {
  id: number;
  productId: number;
  variantId: number;
  quantity: number;
  totalPrice: number;
};

export type DiscountCode = {
  code: string;
  discountPercentage: number;
  expirationDate: Date;
};

export type PaymentMethod = {
  id: number;
  name: string;
  type: string;
};

export type Payment = {
  id: number;
  orderId: number;
  paymentMethodId: number;
  paymentDate: Date;
  amount: number;
};